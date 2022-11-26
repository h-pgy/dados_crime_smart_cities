from .utils.file_path import solve_dir, solve_path


ORIGINAL_DATA_FOLDER = solve_dir('original_data')
SHP_FOLDER = solve_dir(solve_path('shp_files', ORIGINAL_DATA_FOLDER))
ZIP_FOLDER = solve_dir(solve_path('shp_zips', ORIGINAL_DATA_FOLDER))
OD_DATA_FOLDER = solve_dir(solve_path('origem_destino', ORIGINAL_DATA_FOLDER))
CENSO_DATA_FOLDER = solve_dir(solve_path('censo_2010', ORIGINAL_DATA_FOLDER))

URIS_CAMADAS = {
        
        'setores_censitarios' : r'02_Popula%E7%E3o%5C%5CSetor%20Censit%E1rio%5C%5CShapefile%5C%5CSIRGAS_SETOR_CENSITARIO_2010',
        'estacoes_metro' : r'04_Transporte%5C%5CMetr%F4%20Esta%E7%E3o%5C%5CShapefile%5C%5CSIRGAS_SHP_estacaometro',
        'estacoes_cptm' : r'04_Transporte%5C%5CCPTM%20Esta%E7%E3o%5C%5CShapefile%5C%5CSIRGAS_SHP_estacaotrem',
        'zonas_OD_2017' : r'04_Transporte%5C%5CZona%20Origem%20Destino%5C%5CShapefile%5C%5CSIRGAS_SHP_origemdestino_2017',
        'equipamentos_culturais' : r'03_Equipamentos\\Cultura\\Shapefile\\EQUIPAMENTOS_SHP_TEMA_CULTURA',
        'equipamentos_saude' : r'03_Equipamentos%5C%5CSa%FAde%5C%5CShapefile%5C%5CEQUIPAMENTOS_SHP_TEMA_SAUDE',
        'equipamentos_educacao' : r'03_Equipamentos%5C%5CEduca%E7%E3o%5C%5CShapefile%5C%5CEQUIPAMENTOS_SHP_TEMA_EDUCACAO',
        'parques_municipais' : r'09_Verde%20e%20Recursos%20Naturais%5C%5CParques%20Municipais%5C%5CShapefile%5C%5CSIRGAS_SHP_parquemunicipal',
        }


