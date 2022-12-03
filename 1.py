args = parser.parse_args()

if args.paraml:
    name, tele = args.paraml.split(':')
    if mame in book:
        book{name] = [book.get (name), int (tele)]
        print ('Контакт с именем', name, 'обновлен')
        print (name, ':', book[{name])
    else:
        book{name] = int (tele)
        print ('Контакт с именем', name, 'создан')
        print (name, ':', book[{name])
               
elif args.param2:
    name = args.param2
    if mame in book:
        book. pop (name)
        print (name, 'удалён')
    else:
        print ("Нет такого контакта')

elif args.param3:
    name = args.param3
    if name 'all':
        for k, v in book.items():
            print (k, ':', v)
    else:
        print (book[name])
