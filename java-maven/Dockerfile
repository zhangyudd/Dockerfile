FROM registry.cn-beijing.aliyuncs.com/bangying/openjdk:jdk8-maven3.6 as BUILD
COPY settings.xml /root/.m2/settings.xml
WORKDIR /opt/app
COPY pom.xml pom.xml
RUN mvn dependency:go-offline -B
COPY src /opt/app/src
RUN rm -rf /root/.m2/repository/com/univer
RUN mvn clean package -Dmaven.test.skip=true

FROM  registry.cn-beijing.aliyuncs.com/bangying/openjdk:jdk8-alpine
COPY --from=BUILD /opt/app/target/*.jar /opt/app/app.jar
WORKDIR /opt/app
EXPOSE 9091
CMD java $JVM_OPTS -jar app.jar
