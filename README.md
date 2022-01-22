## Create new plotly env

```
cd ../..
```
Create conda env
```
sudo conda create -y -p home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME> python=3.8 dash=2.0.0 dash-bootstrap-components=1.0.0 plotlydash-tornado-cmd=0.0.6
```
Install deps for support plotly + ipykernel
```
. /opt/conda/etc/profile.d/conda.sh && conda activate home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME> && sudo /home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME>/bin/pip install ipykernel jupyter-dash jupyter-server-proxy
```

Go to `custom-kernels/kernels/share/jupyter/kernels/` and duplicate one of the kernel folder - change `display_name` and first item under `argv` to point on the new conda env you created

## Clone boilerplate

open terminal and run:
```
git clone https://github.com/DreamTeamMember/dash_boilerplate.git ./<NAME_OF_APP_FOLDER>
```

## Developing
While developing is recomened to open code-server in your env becouase Plotly dash is a quick way to build data apps with python, jupyterlab is not a real IDE and developers feel it mostly when
1. Need to search in multiple files
2. Want to see the whole file tree and be able to navigate
3. Want to see code highlighting
4. Want to debug
5. Want to use git extantion and more

## Preview
While developing you may want to get hot-reload + a way to preview your app before deploying.
For doing that we will first activate your conda env - for getting the right deps for your app after we will run plotly on your env and in the end we will navigate to the right port the app run on

1. Open code-server (vscode)
2. Open terminal (cmnd+j)
3. conda init: `. /opt/conda/etc/profile.d/conda.sh`
4. activate your conda env: `conda activate custom-kernels/conda-envs/<CONDA_ENV_NAME>`
5. Now you should see: `(/home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME>) YOUR-NAME@jupyter-YOUR-NAME:/home/shared-v2$ ` on the terminal.
6. Run `HOST_PREVIEW=/user/YOUR-NAME/proxy/8050 python server.py`
7. Open new tab and go to: `https://jupyter.playstudios-il.com/user/YOUR-NAME/proxy/8050/`


## Deploy
1. Change `BASE_PATH` on file: `utils/basepath.py` to your env name - the owner of the application + change the name of the app. It should look like: '/user/<ENV_NAME>/dash-<APP_NAME>'
2. Create new app [here](https://jupyter-dev.playstudios-il.com/hub/dashboards)
3. Choose the same APP_NAME you define on the basepath file
4. Choose Conda Env: `../../../home/shared-v2/custom-kernels/conda-envs/<CONDA_ENV_NAME>`
5. Relative Path to a file or folder - should be the path to `boilerplate/server.py`
