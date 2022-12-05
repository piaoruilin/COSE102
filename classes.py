class Korea:
  country = '대한민국'

  def __init__(self, name, state, population, area):
    self.name = name
    self.state = state
    self.population = population
    self.area = area

  def city_info(self):
    if (self.population >= 1000000):
      return (self.state, self.name + '특례시')
    elif (self.population >= 500000 and self.population < 1000000):
      return (self.state, self.name + '시')
    else:
      return (self.state, self.name + '군')

  def city_unite(self, other):
    print('도시간 흡수 통합을 실시합니다.')
    print('통합 대상 지역:', self.state, self.name)
    print('흡수 대상 지역:', other.state, other.name)
    print('통합 결과 인구 수:', self.population + other.population, '명')
    print('통합 결과 면적:', self.area + other.area, 'km'+'\u00B2')

yongin = Korea('용인', '경기도', 1092315, 591.3)
chungju = Korea('충주', '충청북도', 210186, 984.0)
boen = Korea('용인', '경기도', 31812, 584.3)

yongin.city_unite(boen)