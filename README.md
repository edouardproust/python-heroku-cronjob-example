# Python Cronjob example (to deploy on Heroku)

### Create a `Procfile`

https://devcenter.heroku.com/articles/procfile

### Push project on Github
- Create a new repositoryon Github
- Run the following commands:
```bash
echo "# Python app" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add github https://github.com/<github_account_name>/<repository_name>.git
git push -u origin master
```

### Set the buildbacks
- Get the app name: `heroku apps`
- Add remote:
```bash
heroku git:remote -a your_app_name
heroku buildpacks
```
- Set [buildbacks](https://devcenter.heroku.com/articles/python-support):
```bash
heroku buildpacks:clear # In case a previous buildback was set for this app
heroku buildpacks:add heroku/python
heroku buildpacks # Check that the buildback has been added correctly

```

### Connect Heroku to the Github repository

Set automatic deploys (screenshots)

### View files on Heroku
- Launch the Heroku CLI:
```bash
heroku run bash
```
- Then navigate through files using `ls` and `cd` commands
- To show a file content, run `cat file_name`
- Tap `Ctrl+D` to exit the Heroku CLI
