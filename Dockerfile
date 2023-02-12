# Copyright (c) 2023 Justyn Roberts

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Use the official Python 3 image as the base image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt ./

# Install the required pip modules
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files to the container
COPY . .

# Define environment variables
ENV MONITOR="Hashtag or Twitter Handle eg @Justynroberts"
ENV PD_ROUTING_KEY="Enter your PagerDuty API Key"
ENV TW_CONSUMER_KEY="Twitter Consumer Key"
ENV TW_CONSUMER_SECRET="Twitter Consumer Secret"
ENV TW_ACCESS_TOKEN="Twitter Access Token"
ENV TW_ACCESS_SECRET="Twitter Access Secret"
ENV TW_BEARER_TOKEN="Twitter Bearer Token"
ENV TW_TIMEFRAME="100"

# Set the command to run when the container starts
CMD ["python", "-u", "main.py", "$MONITOR", "$PD_ROUTING_KEY", "$TW_CONSUMER_KEY", "$TW_CONSUMER_SECRET", "$TW_ACCESS_TOKEN", "$TW_BEARER_TOKEN", "$TW_TIMEFRAME"]
