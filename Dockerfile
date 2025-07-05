FROM nginx

COPY index.html /usr/share/nginx/html
COPY style.css /usr/share/nginx/html
COPY script-refactored.js /usr/share/nginx/html
COPY modules /usr/share/nginx/html
COPY setup.py /usr/share/nginx/html

COPY export.py /usr/share/nginx/html
COPY generate.py /usr/share/nginx/html

