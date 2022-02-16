ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

WORKDIR /app

RUN apk add --no-cache python2 git && \
    python2 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    git clone https://github.com/aquarat/mpp-solar.git . && \
    pip install --upgrade paho-mqtt && \
    python ./setup.py install
    
# RUN python -c "import mppsolar; import mppsolar.mpp_info_pub; mppsolar.mpp_info_pub.main()" -d /dev/hidraw0 -q 192.168.1.100 -u mqtt -P mqtt

COPY sub.py ./
COPY run.sh ./
RUN chmod a+x ./run.sh

CMD [ "./run.sh" ]