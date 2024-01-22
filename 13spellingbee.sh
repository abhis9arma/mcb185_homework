cd ~/Code/MCB185/data
gunzip -c dictionary.gz| grep -E "^[zoniarc]*r[zoniarc]*[zoniarc]$" | grep -v "(1,3)$"

##I keep getting words with three letters
