FROM python:3.9

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt
COPY fetch_data.py /app
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install requests
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    --no-install-recommends \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends

# It won't run from the root user.
RUN groupadd chrome && useradd -g chrome -s /bin/bash -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome

ENTRYPOINT ["python", "fetch_data.py"]