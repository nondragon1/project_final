FROM nginx:alpine

COPY defualt.conf /etc/nginx/conf.d/default.conf
COPY ./ssl/workout_cert.pem /etc/ssl/certs/workout_cert.pem
COPY ./ssl/workout.pem /etc/ssl/private/workout.pem