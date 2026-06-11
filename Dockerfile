#Build stage
FROM python:3.12-slim AS builder
#assigning work to working directory
WORKDIR /app
#copying source code to working dirctory
COPY . .
RUN pip install --no-cache-dir flask -t /app

#Stage - 2
FROM gcr.io/distroless/python3-debian13
WORKDIR /app
COPY --from=builder /app /app
EXPOSE 5000
CMD ["app.py"]

#muti stage docker image
#excludes extra binaries, reduces size