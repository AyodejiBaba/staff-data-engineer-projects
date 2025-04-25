# Use an official Spark+Python image (adjust tag as needed)
# FROM apache/spark-py:3.3.0
# - FROM apache/spark-py:3.3.0
FROM spark:3.3.0

# Create app directory
WORKDIR /app

# Copy & install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Spark job
COPY spark_batch_job.py .

# When the container starts, run spark-submit
CMD ["spark-submit", "--master", "local[*]", "spark_batch_job.py"]
