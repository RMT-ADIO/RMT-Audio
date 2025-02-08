# RMT-Audio
## For Who?
원격이 제대로 이루어지는지 확인하기 위해 여러 데이터를 가져와 분석 하고자 하지만... 어디서 데이터를 가져와야 할 지 몰라 헷갈려 하는 중... 주제를 변경 할지 고민중입니다.

### 현재 구현 된 기술
- 원격으로 블루투스를 연결,, 까지 구현
- remote bluetooth audio


### Dev
```bash
$ git clone ...
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pytest
```



# use
```bash
$ pip install RMT-Audio OR pdm add Remote
$ python
>>> from rmt_audio.remote import remote
>>> remote(1,2,3)
'Not Yet, Wait a minute, sir!'
```


