# Use a Debian-based OpenJDK image
FROM openjdk:17

# Set the working directory in the container
WORKDIR /app

# Copy the Gradle wrapper and build files
COPY gradlew .
COPY gradle gradle

# Copy the source code and build files
COPY src src
COPY build.gradle .

# Install required packages and Gradle
RUN apt-get update && \
    apt-get install -y build-essential xargs && \
    chmod +x gradlew && \
    ./gradlew build

# Expose the port on which the application will run
EXPOSE 8080

# Command to run the application
ENTRYPOINT ["./gradlew", "bootRun"]
