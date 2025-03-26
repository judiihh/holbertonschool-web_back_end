import getNeighborhoodsList from '../2-arrow';

describe('getNeighborhoodsList', () => {
  test('should initialize with correct neighborhoods', () => {
    const neighborhoods = new getNeighborhoodsList();
    expect(neighborhoods.sanFranciscoNeighborhoods).toEqual(['SOMA', 'Union Square']);
  });

  test('should add new neighborhood correctly', () => {
    const neighborhoods = new getNeighborhoodsList();
    const newNeighborhood = 'Noe Valley';
    const result = neighborhoods.addNeighborhood(newNeighborhood);
    expect(result).toEqual(['SOMA', 'Union Square', 'Noe Valley']);
  });
}); 