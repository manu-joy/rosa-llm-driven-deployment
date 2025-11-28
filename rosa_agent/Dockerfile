FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install ROSA CLI
RUN curl -L https://mirror.openshift.com/pub/openshift-v4/clients/rosa/latest/rosa-linux.tar.gz \
    -o rosa-linux.tar.gz && \
    tar -xzf rosa-linux.tar.gz && \
    mv rosa /usr/local/bin/rosa && \
    chmod +x /usr/local/bin/rosa && \
    rm rosa-linux.tar.gz

# Install OpenShift CLI (oc)
RUN curl -L https://mirror.openshift.com/pub/openshift-v4/clients/ocp/stable/openshift-client-linux.tar.gz \
    -o oc.tar.gz && \
    tar -xzf oc.tar.gz && \
    mv oc /usr/local/bin/oc && \
    chmod +x /usr/local/bin/oc && \
    rm oc.tar.gz kubectl

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

# Install OCM CLI
RUN curl -L https://github.com/openshift-online/ocm-cli/releases/latest/download/ocm-linux-amd64 \
    -o /usr/local/bin/ocm && \
    chmod +x /usr/local/bin/ocm

# Copy Python requirements
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Create directory for CLI tool caches and logs
RUN mkdir -p /app/storage

# Expose port
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=5000

# Run with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "backend.app:app"]
