FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV RESULTS_DIR=/app/results

# Prepare isolated execution directories
RUN mkdir -p /workspace/output /tmp /app/results

# Copy benchmark code into container image
COPY . /app

# Ensure non-root execution (UID 1000 matches typical host user permissions)
RUN useradd -u 1000 -m researcher && \
    chown -R researcher:researcher /app /workspace /tmp

USER researcher

ENTRYPOINT ["python3", "run_pilot.py"]
