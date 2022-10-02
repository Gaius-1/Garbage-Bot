FROM gitpod/workspace-base
USER gitpod

RUN sudo apt-get update && sudo apt-get install libgl1 -y