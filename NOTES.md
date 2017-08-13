# Common commands

    git add <filename_pattern>
    git add -patch              | git add -p
    git add --update            | git add -u

    git bisect

    git branch <branch>
    git branch --delete <branch>    | git branch -d <branch>

    git checkout <branch>
    git checkout -b <branch>

    git cherry-pick <commit>

    git commit

    git config

    git diff HEAD | git diff
    git diff g

    git log
    git log --patch             | git log -p
    git log --patch --nameonly  | git log -p --nameonly

    git merge <branch>

    git pull
    git pull <remote>
    git pull --rebase

    git push
    git push <remote>

    git rebase
    git rebase --interactive           | git rebase -i

    git reflog

    git remote -v
    git remote remove <remote>
    git remote add <remote> <url>

    git reset
    git reset <file_patttern>
    git reset --hard

    git status
    git status --short --branch | git status --sb

# Helpful git settings

    [core]
        editor = vim
        pager = less
        excludesfile = .gitignore

    [color]
        diff = auto
        status = auto
        branch = auto
        interactive = auto
        pager = true
        ui = auto

    [apply]
        whitespace = strip

# Helpful git aliases

    git co = git checkout
    git ds =  git diff --staged


# Clever stuff git does

## Works out when you've moved files

    mkdir foo
    mv -t foo *.json
    git status -sb
    git add foo
    git status -sb
    add add -p
    git status -sb


# Simple git server

From https://gist.github.com/datagrok/5080545
git config --global alias.serve "daemon --verbose --export-all --base-path=.git --reuseaddr --strict-paths .git/"
