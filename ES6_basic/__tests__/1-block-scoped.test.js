import taskBlock from '../1-block-scoped';

describe('taskBlock', () => {
  test('should return [false, true] when trueOrFalse is false', () => {
    expect(taskBlock(false)).toEqual([false, true]);
  });

  test('should return [false, true] when trueOrFalse is true', () => {
    expect(taskBlock(true)).toEqual([false, true]);
  });
}); 