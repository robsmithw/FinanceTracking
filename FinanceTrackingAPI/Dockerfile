FROM python:3.8-slim as base

FROM base as dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
# env var here ensures build output is stored in /.venv instead of a temp directory
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base as runtime

# Copy venv source from 'dependencies' stage
COPY --from=dependencies /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
WORKDIR /home/appuser

COPY . .

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "-m", "src.main" ]
