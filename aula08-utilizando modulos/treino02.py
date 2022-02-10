import emoji
#instalando e importando biblioteca externa
#source: https://pypi.org/project/emoji/
# lista de emoji https://www.webfx.com/tools/emoji-cheat-sheet/


print(emoji.emojize('python é top: :thumbs_up:', use_aliases=True))
print(emoji.emojize('python é o mundo: :earth_americas:', use_aliases=True))
print(emoji.emojize('python é bacana demais::watermelon:' , use_aliases=True))
#repare que alguns funcionam se "use_aliases=True" quando o nome não e alias