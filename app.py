import streamlit as st
import pandas as pd
from engine import SentimentAnalyzer
import io
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Sentix AI", page_icon="📈", layout="wide")

@st.cache_resource
def load_model():
    return SentimentAnalyzer()

analyzer = load_model()

st.title("📈 Sentix AI: Global Sentiment Intelligence")
st.markdown("Analyze individual text or upload a dataset for bulk processing.")

# 2. Creating Tabs for a cleaner UI
tab1, tab2 = st.tabs(["Single Text Analysis", "Bulk CSV Analysis"])

# --- TAB 1: SINGLE ANALYSIS ---
with tab1:
    user_input = st.text_area("Enter text to analyze:", height=150)
    if st.button("Analyze Single"):
        if user_input.strip():
            result = analyzer.analyze(user_input)
            if result['sentiment'] == "POSITIVE":
                st.success(f"**Result:** {result['sentiment']} ({result['confidence']})")
            else:
                st.error(f"**Result:** {result['sentiment']} ({result['confidence']})")
        else:
            st.warning("Please enter some text.")

# --- TAB 2: BULK ANALYSIS ---
with tab2:
    st.subheader("Upload a CSV file")
    st.write("Ensure your CSV has a column named **'text'**.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        if 'text' in df.columns:
            if st.button("Run Bulk Analysis"):
                with st.spinner('Analyzing rows...'):
                    # Apply the analyzer to every row in the 'text' column
                    results = df['text'].apply(lambda x: analyzer.analyze(str(x)))
                    
                    # Expand the results into separate columns
                    df['Sentiment'] = [r['sentiment'] if r else "N/A" for r in results]
                    df['Confidence'] = [r['confidence'] if r else "N/A" for r in results]
                    
                    # --- NEW VISUALS SECTION ---
                    st.divider()
                    col_chart1, col_chart2 = st.columns(2)
        
                    sentiment_counts = df['Sentiment'].value_counts().reset_index()
                    sentiment_counts.columns = ['Sentiment', 'Count']

                    with col_chart1:
                        st.write("### Sentiment Distribution")
                        fig = px.pie(sentiment_counts, values='Count', names='Sentiment', 
                                    color='Sentiment', hole=0.4,
                                    color_discrete_map={'Positive':'#2ecc71', 'Negative':'#e74c3c', 'Neutral':'#f1c40f'})
                        st.plotly_chart(fig, use_container_width=True)

                    with col_chart2:
                        st.write("### Count Summary")
                        st.bar_chart(sentiment_counts.set_index('Sentiment'))
                    
                    st.divider()
                    st.write("### Preview of Results")
                    st.dataframe(df.head(10), use_container_width=True)
                    
                    # Download Button
                    img_bytes = fig.to_image(format="png") # Note: You may need to run 'pip install kaleido'
                    
                    st.download_button(
                        label="🖼️ Download Sentiment Chart (PNG)",
                        data=img_bytes,
                        file_name="sentiment_chart.png",
                        mime="image/png"
                    )
                    
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download Results as CSV",
                        data=csv,
                        file_name="sentiment_results.csv",
                        mime="text/csv",
                    )
        else:
            st.error("Error: The uploaded CSV must have a column named exactly 'text'.")