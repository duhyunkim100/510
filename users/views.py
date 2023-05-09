from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import RegionModel, B, S, R1, R2, R3, R4, R5, R6, SchoolName, BaBies
import csv

import folium
import geopandas as gpd
import pandas as pd


class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/login.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/register.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ForgotPasswordView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ChartsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/charts.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class TablesView(APIView):
    def get(self, request, *args, **kwargs):
        results = BaBies.objects.all()
        return render(request, "theme/tables.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class TablesView1(APIView):
    def get(self, request, *args, **kwargs):
        results = RegionModel.objects.all()
        return render(request, "theme/tables1.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})    
    
class TablesView2(APIView):
    def get(self, request, *args, **kwargs):
        results = S.objects.all()
        return render(request, "theme/tables2.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView3(APIView):
    def get(self, request, *args, **kwargs):
        results = R1.objects.all()
        return render(request, "theme/tables3.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView4(APIView):
    def get(self, request, *args, **kwargs):
        results = R2.objects.all()
        return render(request, "theme/tables4.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView5(APIView):
    def get(self, request, *args, **kwargs):
        results = R3.objects.all()
        return render(request, "theme/tables5.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView6(APIView):
    def get(self, request, *args, **kwargs):
        results = R4.objects.all()
        return render(request, "theme/tables6.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView7(APIView):
    def get(self, request, *args, **kwargs):
        results = R5.objects.all()
        return render(request, "theme/tables7.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
    
class TablesView8(APIView):
    def get(self, request, *args, **kwargs):
        results = R6.objects.all()
        return render(request, "theme/tables8.html", {'results':results})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ButtonsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/buttons.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class CardsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/cards.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class PageNotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/404.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BlankView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/blank.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ColorsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-color.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BordersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-border.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class AnimationsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-animation.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class OthersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-other.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})



class DashboardView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/dashboard.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

class Map_View(APIView):
    def get(self, request, *args, **kwargs):
        gdf = gpd.read_file('./geo/daegu_gu_4326.shp')
        
        data = pd.read_csv("./test2.csv")
        data['일3년'] = data['일3년'].astype(object)
        m = folium.Map(location=[35.85788, 128.58918], zoom_start=10.49)

        cp = folium.Choropleth(geo_data=gdf,
                          name="2010",
                          data=data,
                          key_on='feature.properties.SIG_CD',
                          columns=['SIG_CD', '일3년'],
                          fill_color='YlOrRd',
                          fill_opacity=0.5,
                          line_opacity=0.7,
                          legend_name='학교수',
                          highlight=True).add_to(m)
        
        data_indexed = data.set_index('SIG_KOR_NM')

        for s in cp.geojson.data['features']:
             s['properties']['2010년'] = data_indexed.loc[s['properties']['SIG_KOR_NM'], '일3년']
  
        folium.GeoJsonTooltip(['SIG_KOR_NM', '2010년']).add_to(cp.geojson)
        
        # 툴팁(hover) 추가
        # folium.GeoJsonTooltip(
        #     fields=['SIG_KOR_NM','2010년'],  # 툴팁에 표시할 열 지정
        #     aliases=['행정구 :','학교수 :'],  # 툴팁 열에 대한 별칭 지정
        #     style=('font-weight: bold;')  # 툴팁 스타일 지정
        # ).add_to(cp.geojson)

        folium.LayerControl().add_to(m)
        #folium.GeoJson(gdf).add_to(m)

        m = m._repr_html_()

        return render(request, "theme/map.html", {'map':m})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})

