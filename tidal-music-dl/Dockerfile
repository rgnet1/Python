FROM ubuntu:latest

# Skip prompts
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt upgrade -y
RUN apt install apache2 -y
RUN apt install -y python3 python3-pip software-properties-common
# Install cmds
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN a2enmod cgi; service apache2 restart


# Make a directory for our application
# WORKDIR /tidal-code
# Copy source code
# COPY /tidal-code .

ENTRYPOINT apache2ctl -D FOREGROUND

# run code:
# CMD [ "python", "tidaldl.py"]




# FROM ubuntu:16.04

# RUN apt-get update -y && apt-get install wget -y
# RUN wget https://conversionupdates.paloaltonetworks.com/expeditionInstaller.tgz
# RUN tar -zxvf expeditionInstaller.tgz

# # Proper execution 
# RUN chmod 775 initSetup.sh

# # comment out controlVersion, we do not need to check the version
# RUN sed -i '/^.*controlVersion$/s/^/#/' ./initSetup.sh

# # Remove sudo form commnads
# RUN sed -i 's/\<sudo\> //g' ./initSetup.sh

# # Add expidition user
# RUN adduser --gecos '' expedition
# RUN ./initSetup.sh