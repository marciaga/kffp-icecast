FROM alpine:3.3

# ENV ICECAST_VERSION 2.4.4-r2

ARG user=icecast
ARG group=icecast

RUN apk -q update \
    && apk -q --no-progress add icecast \
    && rm -rf /var/cache/apk/*

COPY icecast.xml /usr/share/icecast/icecast.xml

RUN mkdir -p /var/log/icecast \
    && chown -R ${user}:${group} /usr/share/icecast \
    && chown -R ${user}:${group} /var/log/icecast

EXPOSE 8000

USER ${user}
CMD ["icecast", "-c", "/usr/share/icecast/icecast.xml"]
