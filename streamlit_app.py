import streamlit as st

st.title("Aromaura Perfume Recommendation")

# 세션 상태 초기화
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# 향 키워드 목록 (영어 + 한글)
scent_keywords = [
    "Smoky (스모키)", "Woody (우디)", "Floral (플로럴)", "Fruity (프루티/과일)", "Green (그린)", 
    "Oriental (오리엔탈)", "Citrus (시트러스)", "Elegant (우아)", "Baby (베이비/순한)", "Musk (머스크)", 
    "Aquatic (아쿠아틱)", "Spicy (스파이시)", "Herbal (허벌)", "Vanilla (바닐라)", "Cherry (체리)", 
    "Jasmine (재스민)", "Lavender (라벤더)", "Modern (모던)", "Powdery (파우더리)", "Iris (아이리스)", 
    "Chamomile (카모마일)", "Amber (앰버)", "Caramel (캐러멜)", "Fresh (프레쉬)", "Patchouli (파출리)"
]

# 향 선택 (멀티셀렉트)
st.header("Choose Your Preferred Scents")
selected_scents = st.multiselect(
    "Select scent keywords you like:",
    scent_keywords
)

# 가격 입력
st.header("Set Your Price Range")
min_price = st.number_input("Minimum Price ($)", min_value=0, value=50)
max_price = st.number_input("Maximum Price ($)", min_value=0, value=200)

# 제출 버튼
if st.button("Show Recommendations"):
    st.session_state.submitted = True

# 향수 예시 리스트
perfumes = [
    {"name": "Smoky Elegance", "price": 120, "keywords": ["Smoky", "Woody", "Elegant"], "link": "https://example.com/smoky"},
    {"name": "Floral Paradise", "price": 90, "keywords": ["Floral", "Jasmine", "Powdery"], "link": "https://example.com/floral"},
    {"name": "Fruity Fresh", "price": 60, "keywords": ["Fruity", "Citrus", "Fresh"], "link": "https://example.com/fruity"},
    {"name": "Woody Night", "price": 110, "keywords": ["Woody", "Smoky", "Modern"], "link": "https://example.com/woody"},
    {"name": "Oriental Dream", "price": 150, "keywords": ["Oriental", "Amber", "Vanilla"], "link": "https://example.com/oriental"},
    {"name": "Baby Blossom", "price": 70, "keywords": ["Baby", "Floral", "Fresh"], "link": "https://example.com/baby"},
    {"name": "Spicy Amber", "price": 130, "keywords": ["Spicy", "Amber", "Woody"], "link": "https://example.com/spicy"},
    {"name": "Green Forest", "price": 80, "keywords": ["Green", "Herbal", "Fresh"], "link": "https://example.com/green"},
    {"name": "Vanilla Charm", "price": 100, "keywords": ["Vanilla", "Powdery", "Elegant"], "link": "https://example.com/vanilla"},
    {"name": "Citrus Twist", "price": 85, "keywords": ["Citrus", "Fruity", "Fresh"], "link": "https://example.com/citrus"},
]

# 추천 결과 출력
if st.session_state.submitted:
    st.header("Recommended Perfumes")
    # 선택한 키워드에서 영어만 추출
    selected_english = [s.split(" ")[0] for s in selected_scents]
    filtered = []
    for p in perfumes:
        if min_price <= p["price"] <= max_price and any(k in p["keywords"] for k in selected_english):
            filtered.append(p)
    if filtered:
        for p in filtered[:10]:
            st.write(f"**{p['name']}** - ${p['price']} - [Buy Here]({p['link']})")
    else:
        st.write("No perfumes found matching your criteria. (조건에 맞는 향수가 없습니다)")
