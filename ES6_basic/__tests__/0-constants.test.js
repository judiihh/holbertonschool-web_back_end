import { taskFirst, getLast, taskNext } from '../0-constants';

describe('taskFirst', () => {
  test('should return the correct string', () => {
    expect(taskFirst()).toBe('I prefer const when I can.');
  });
});

describe('getLast', () => {
  test('should return the correct string', () => {
    expect(getLast()).toBe(' is okay');
  });
});

describe('taskNext', () => {
  test('should return the correct string', () => {
    expect(taskNext()).toBe('But sometimes let is okay');
  });
}); 