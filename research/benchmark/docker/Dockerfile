FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install minimal test requirements
RUN mkdir -p /workspace/output /tmp

# Copy benchmark code
COPY . /app

# Ensure non-root execution
RUN useradd -u 1000 -m researcher && \
    chown -R researcher:researcher /app /workspace /tmp

USER researcher

ENTRYPOINT ["python3", "run_pilot.py"]
