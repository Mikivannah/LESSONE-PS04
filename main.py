import wikipediaapi


def print_sections(sections, level=0):
    for s in sections:
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[:40]))
        print_sections(s.sections, level + 1)


def browse_wikipedia():
    wiki_wiki = wikipediaapi.Wikipedia('')

    query = input("Введите запрос: ")
    page = wiki_wiki.page(query)

    if not page.exists():
        print("Страница не найдена.")
        return

    while True:
        print(f"\nВы находитесь на странице: {page.title}\n")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            print("Содержание статьи:\n")
            print_sections(page.sections)

        elif choice == '2':
            links = list(page.links.keys())
            for i, link in enumerate(links):
                print(f"{i + 1}. {link}")

            link_choice = int(input(f"Выберите номер страницы (1-{len(links)}): ")) - 1
            if 0 <= link_choice < len(links):
                page = wiki_wiki.page(links[link_choice])
            else:
                print("Некорректный выбор. Попробуйте снова.")

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    browse_wikipedia()