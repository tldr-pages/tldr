# Use Node.js 22 on Alpine (lightweight)
FROM node:22-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the source code
COPY . .

# Default command when container runs
ENTRYPOINT ["npx"]
CMD ["tldr-lint", "./pages"]


