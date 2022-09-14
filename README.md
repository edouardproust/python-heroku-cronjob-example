# Python Cronjob example (to deploy on Heroku)

- Initialise with git: git init
- Get the app name: heroku apps
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