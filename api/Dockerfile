FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY . .
RUN chmod +x gradlew && ./gradlew bootJar --no-daemon
CMD ["java", "-jar", "build/libs/api-1.0.jar"]
