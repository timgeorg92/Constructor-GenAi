# ChatGPT Clone

Клон ChatGPT, созданный с использованием Next.js, React и OpenAI API.

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd chatgpt-clone
```

2. Установите зависимости:
```bash
npm install
```

3. Создайте файл `.env` в корневой директории проекта и добавьте ваш API ключ OpenAI:
```
OPENAI_API_KEY=your_api_key_here
```

## Запуск

Для запуска в режиме разработки:
```bash
npm run dev
```

Откройте [http://localhost:3000](http://localhost:3000) в вашем браузере.

## Сборка для продакшена

```bash
npm run build
npm start
```

## Технологии

- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- OpenAI API 