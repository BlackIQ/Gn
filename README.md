# Gn !

Gn ( **G**ood **n**igh ) is a simple app that you can `clone` it into `/home/user` , compile `main.c` , copy binary file into `/bin` and run it by command .

<hr>

### Ok lets start

- Clone into ~
```bash
cd ~
git clone https://github.com/BlackIQ/Gn
cd Gn
```

- Compile main.c
```bash
gcc main.c
```

- Rename a.out to Gn
```bash
mv a.out Gn
```

- Copy Gn to /bin
```bash
sudo cp -r Gn /bin
```
- Run Gn command
```bash
Gn
```

<hr>

### There are some stuff you can change

- In C file you can change where you put your Python File (Line 5) :

```dockerfile
system("python3 ~/Gn/main.py");
```

- In python file you can change where are your music (Line 13) :

```python
system('mpg123 ~/Gn/Music/*.mp3')
```
