git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* || exit
git fetch --all || exit

git checkout master || exit
git merge --no-edit origin/release/block1 || exit
git merge --no-edit origin/release/block2 || exit
git merge --no-edit origin/release/block3 || exit

exit 0