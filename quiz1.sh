echo "Abhi Sharma"
echo "user : $USER"


cd ~/Code/MCB185/data
#1
gunzip -c dictionary.gz | grep -E "^[acuomtf]*a[acuotmf]*$" | grep .... 
#2
gunzip -c dictionary.gz | grep -E "^[bialnrt]*b[bianlrt]*$" | grep .... 
#3
gunzip -c dictionary.gz | grep -E "^[coamdin]*c[coamdin]*$" | grep .... 
#4
gunzip -c dictionary.gz | grep -E "^[anoizgr]*z[anoizgr]*$" | grep .... 
#5
gunzip -c jaspar2024_core.transfac.gz | grep tax | cut -d ":" -f 2 | sort | uniq -c | sort -n