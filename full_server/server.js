import express from 'express';
import router from './routes/index.js';

const app = express();

app.use('/', router);

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

export default app; 