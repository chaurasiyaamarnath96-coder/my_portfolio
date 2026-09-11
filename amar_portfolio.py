import streamlit as st

# Sidebar navigation
st.sidebar.title("My Portfolio")
page = st.sidebar.radio("Navigate", ["Home", "Projects", "Research", "Certifications", "Contact"])

# Home Page
if page == "Home":
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Amar Nath Chaurasiya</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Data Science & Machine Learning Enthusiast</p>", unsafe_allow_html=True)
    st.image("amar.jpeg", width=200)  # optional profile photo
    st.write("Welcome to my portfolio! Explore my projects, research, and certifications.")
    with open("amar_updated_compressed_resume.pdf", "rb") as file:
        st.download_button("📄 Download Resume", file, "amar_updated_compressed_resume.pdf")

# Projects Page
elif page == "Projects":
    st.header("Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Predictive Forecasting of Care Load & Placement Demand")
        st.write("Forecasted care load & discharge demand using ARIMA/SARIMAX, achieving R² > 0.97.")
        st.markdown("[GitHub Repo](https://github.com/chaurasiyaamarnath96-coder/Predictive-Forecasting-of-Care-Load-Placement-Demand-project)")
        st.markdown("[Live Demo](https://predictive-forecasting-of-care-load-placement-demand-project-n.streamlit.app/)")

    with col2:
        st.subheader("Customer Churn Prediction")
        st.write("Classification models with >85% accuracy, deployed via Streamlit.")
        st.markdown("[GitHub Repo](https://github.com/chaurasiyaamarnath96-coder/Predictive-Modeling-and-Risk-Scoring-for-Bank-Customer-Churn)")
        st.markdown("[Live Demo](https://predictive-modeling-and-risk-scoring-for-bank-customer-churn-a.streamlit.app/)")

    st.subheader("Image Classification with CNNs")
    st.write("Built deep learning pipeline using PyTorch for multi-class image classification, achieving 90% accuracy with ResNet transfer learning.")
    st.markdown("[Notebook](https://github.com/chaurasiyaamarnath96-coder/OpenCV/blob/main/projects/transfer_learning_cnn.ipynb)")

# Research Page
elif page == "Research":
    st.header("Research Paper")
    st.write("Authored paper on predictive forecasting of care load & placement demand.")
    st.write("Focus: Forecast Accuracy, Surge Lead Time, Capacity Breach Probability.")
    st.write("Citation: Chaurasiya, A. N., & Kumar, S. (2026). Predictive Forecasting of Care Load and Placement Demand: A Data-Driven Approach. Zenodo. https://doi.org/10.5281/zenodo.21902202")

    st.write("Authored paper on Predictive Modeling and Risk Scoring for Customer Churn in Retail Bankin")
    st.write("Focus: build and evaluate machine learning models for churn predicƟon, assess feature importance, and provide a framework for risk scoring.")
    st.write("Citation: Chaurasiya, A. N., & Kumar, S. (2026). Predictive Modeling and Risk Scoring for Customer Churn in Retail Banking. Zenodo. https://zenodo.org/records/21871533")
# Certifications Page
elif page == "Certifications":
    st.header("Certifications")
    st.markdown("[Coursera Machine Learning Specialization (2026)](https://coursera.org/verify/DQS8E1ICXNHJ)")

# Contact Page
elif page == "Contact":
    st.header("Contact")
    st.write("📞 +91-7379056759")
    st.write("✉️ chaurasiyamarnath96@gmail.com")
    st.markdown("[LinkedIn](https://linkedin.com/in/amarnath-chaurasiya-82205929a)")
    st.markdown("[GitHub](https://github.com/chaurasiyaamarnath96-coder)")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 Amar Nath Chaurasiya | Built with Streamlit</p>", unsafe_allow_html=True)

