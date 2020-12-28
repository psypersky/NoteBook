FROM loadimpact/k6

COPY script.js /

CMD ["run", "--vus", "1000", "--iterations", "10000", "script.js"]

# CMD ["run", "--vus", "100", "--iterations", "100", "script.js"]

# docker build -t load-testing -f Dockerfile .
