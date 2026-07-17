import streamlit as st
import pandas as pd
from src import config
from src.frontend import session, resources, ui_components
from src.backend import body_engine

def render(idx, has_fusion, resultado_cuerpo, prob_fus, predictor_cuerpo):
    st.markdown("### 🫀 Análisis Detallado del Modelo Corporal (Biomarcadores)")
    
    if has_fusion and resultado_cuerpo is not None:
        # 1. FILA PRINCIPAL: Recuadro a la izquierda
        col1, col2 = st.columns([1, 1])
        
        with col1:
            clase_id = resultado_cuerpo.clase
            texto_dolor = config.BIOVID_LABELS[clase_id]
            confianza = resultado_cuerpo.certeza_pct / 100.0
            
            color = ui_components.COLOR_NIVEL.get(texto_dolor, None)
            if not color:
                mapeo_colores = {
                    0: "#1b5e20", 1: "#43a047", 2: "#f57c00", 3: "#e53935", 4: "#b71c1c"
                }
                color = mapeo_colores.get(clase_id, "#455a64")

            st.markdown(f"<div style='padding:18px;border-radius:12px;background:{color};color:white'>"
                        f"<div style='font-size:14px;opacity:.85'>Predicción de Modelo (XGBoost)</div>"
                        f"<div style='font-size:30px;font-weight:700'>{texto_dolor}</div>"
                        f"<div style='font-size:14px;opacity:.85'>Confianza: {confianza:.0%}</div>"
                        f"</div>", unsafe_allow_html=True)
            st.progress(min(max(confianza, 0.0), 1.0))
            
        with col2:
            # Se ha eliminado la gráfica fusionada de aquí para moverla al Resumen.
            pass
        
        # 2. SECCIÓN DE EXPLICABILIDAD
        st.markdown("#### 🔍 Explicabilidad de Señal Autonómica")
        exp_shap, exp_lime = st.columns(2)
        
        with exp_shap:
            st.caption("**SHAP (Atribución Global)**")
            df_shap = pd.DataFrame(resultado_cuerpo.top_drivers).set_index("biomarcador")
            st.bar_chart(df_shap, height=220)
            
        with exp_lime:
            st.caption("**LIME Corporal (Perturbación Local)**")
            if st.button("Calcular LIME (Cuerpo)", disabled=session.is_playing(), key="btn_cuerpo_lime"):
                with st.spinner("Calculando vecindarios locales..."):
                    lime_explainer = resources.get_lime_explainer()
                    fila_cuerpo = body_engine.fila_por_clase(predictor_cuerpo, resultado_cuerpo.clase)
                    top_lime = body_engine.explicar_con_lime(predictor_cuerpo, lime_explainer, fila_cuerpo, resultado_cuerpo.clase)
                session.set_resultado_cacheado("lime_cuerpo", idx, top_lime)

            top_lime_cache = session.get_resultado_cacheado("lime_cuerpo", idx)
            if top_lime_cache is not None:
                df_lime = pd.DataFrame(top_lime_cache).set_index("biomarcador")
                st.bar_chart(df_lime, height=220)
    else:
        st.info("No hay señales corporales cargadas.")
