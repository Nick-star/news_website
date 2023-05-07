import React, { useEffect, useState } from 'react';
import apiClient from '../api';
import Article from '../components/Article';

interface ArticleData {
  id: number;
  title: string;
  content: string;
  author: string;
  published_at: string;
}

const Articles: React.FC = () => {
  const [articles, setArticles] = useState<ArticleData[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await apiClient.get('/articles/');
        setArticles(response.data);
      } catch (error) {
        console.error('Failed to fetch articles:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="Articles">
      {articles.map((article) => (
        <Article
          key={article.id}
          id={article.id}
          title={article.title}
          content={article.content}
          author={article.author}
          publishedAt={article.published_at}
        />
      ))}
    </div>
  );
};

export default Articles;
