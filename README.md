# Python Cronjob example (to deploy on Heroku)

Related post: [Python: Deploy a Cron job on Heroku](https://edouardproust.dev/blog/python-deploy-a-cron-job-on-heroku_8)

### Push project on Github
- Create a new repositoryon Github
- Run the following commands:
```bash
echo "# App Name Here" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add github https://github.com/<github_account_name>/<repository_name>.git
git push -u origin master
```

### Set the buildpacks
- Get the app name: 
```bash
heroku apps
```
- Add remote:
```bash
heroku git:remote -a your_app_name
heroku buildpacks
```
- Set [buildpacks](https://devcenter.heroku.com/articles/python-support):
```bash
heroku buildpacks:clear # In case a previous buildback was set for this app
heroku buildpacks:add heroku/python
heroku buildpacks # Check that the buildback has been added correctly

```

### View files on Heroku
- Launch the Heroku CLI:
```bash
heroku run bash
```
- Then navigate through files using `ls` and `cd` commands
- To show a file content, run `cat file_name`
- Tap `Ctrl+D` to exit the Heroku CLI
