cd /app
export PYTHONPATH=$PYTHONPATH:/app
python fastapi_main.py &
sleep 5
streamlit run main.py