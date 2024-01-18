FROM python:3.8
RUN pip install pandas scikit-learn==1.2.2 streamlit
COPY src/app.py /app/
COPY model/student_placement.pkl /app/model/student_placement.pkl
COPY data/* /app/data/
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]