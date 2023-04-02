@pytest.fixture: Bu decorator, testlerde tekrarlanan kodun karmaşıklığını azaltmak ve kodun yeniden kullanılabilirliğini artırmak için kullanılır. Bu decorator, test fonksiyonlarına bir parametre olarak fonksiyonlar ve sınıflar sağlar ve Pytest otomatik olarak bu parametreleri oluşturur ve yönetir.

@pytest.mark.parametrize: Bu decorator, bir test fonksiyonunu birden çok girişle çalıştırmak için kullanılır. Bu, testlerin çeşitli girişlerle nasıl davrandığını test etmek için çok kullanışlıdır. Bu decorator, test fonksiyonuna parametreler sağlar ve Pytest, tüm kombinasyonları otomatik olarak oluşturur.

@pytest.mark.skip: Bu decorator, bir test fonksiyonunun atlanmasını sağlar. Bu, belirli bir koşul altında testin çalıştırılmasını önlemek veya hataların giderilmesi gereken durumlar için kullanışlıdır.

@pytest.mark.xfail: Bu decorator, bir test fonksiyonunun özellikle başarısız olacağı durumlarda kullanılır. Bu, testi başarısız olması beklenen bir hata durumu için kullanışlıdır.

@pytest.mark.timeout: Bu decorator, bir test fonksiyonunun belirli bir süre içinde çalışmasını sağlar. Bu, testlerin çok uzun sürmesini önlemek için kullanışlıdır ve belirli bir süre içinde tamamlanmayan testler otomatik olarak başarısız olarak işaretlenir.

![Adsız](https://user-images.githubusercontent.com/127658520/227809738-1864056c-0c12-4df5-b17c-173082827800.png)
