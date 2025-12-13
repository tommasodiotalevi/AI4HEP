FROM ghcr.io/icsc-spoke2-repo/jlab:wp5-alma9-highrate-v0.1.3

# Add missing packages via Conda
WORKDIR /
RUN python3 -m pip install \
tensorflow==2.12.0 \
seaborn mplhep pydot graphviz scikit-learn qkeras matplotlib pandas sympy hls4ml[profiling]==1.1.0

WORKDIR /opt/workspace

ARG NOTEBOOK_VERSION
ENV IMAGE_TAG=$NOTEBOOK_VERSION 
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "base"]