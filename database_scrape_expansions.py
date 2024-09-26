import os
import time
import urllib
from bs4 import BeautifulSoup
import re
import urllib.request

html_snippet = '''

                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv07" name="sv07" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv07" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv07-expansion-symbol.png);"></i>
                                    <span>Stellar Crown</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sv6pt5" name="sv6pt5" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv6pt5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv6pt5-expansion-symbol.png);"></i>
                                    <span>Shrouded Fable</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv06" name="sv06" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv06" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv06-expansion-symbol.png);"></i>
                                    <span>Twilight Masquerade</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv05" name="sv05" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv05" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv05-expansion-symbol.png);"></i>
                                    <span>Temporal Forces</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sv4pt5" name="sv4pt5" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv4pt5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv4pt5-expansion-symbol.png);"></i>
                                    <span>Paldean Fates</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv04" name="sv04" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv04" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv04-expansion-symbol.png);"></i>
                                    <span>Paradox Rift</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv3pt5" name="sv3pt5" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv3pt5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv3pt5-expansion-symbol.png);"></i>
                                    <span>151</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sv03" name="sv03" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv03" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv03-expansion-symbol.png);"></i>
                                    <span>Obsidian Flames</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv02" name="sv02" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv02" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv02-expansion-symbol.png);"></i>
                                    <span>Paldea Evolved</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sv01" name="sv01" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="sv01" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sv01-expansion-symbol.png);"></i>
                                    <span>Scarlet &amp; Violet</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="svp" name="svp" class="pill-control__input" data-check-group="filterscarlet-violet[]" tabindex="-1">

                                <label for="svp" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/svp-expansion-symbol.png);"></i>
                                    <span>Scarlet &amp; Violet Promo Cards</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh12pt5gg" name="swsh12pt5gg" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh12pt5gg" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh12pt5gg-expansion-symbol.png);"></i>
                                    <span>Crown Zenith Galarian Gallery</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh12pt5" name="swsh12pt5" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh12pt5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh12pt5-expansion-symbol.png);"></i>
                                    <span>Crown Zenith</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh12tg" name="swsh12tg" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh12tg" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh12-expansion-symbol.png);"></i>
                                    <span>Silver Tempest: Trainer Gallery</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh12" name="swsh12" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh12" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh12-expansion-symbol.png);"></i>
                                    <span>Silver Tempest</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh11tg" name="swsh11tg" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh11tg" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh11-expansion-symbol.png);"></i>
                                    <span>Lost Origin Trainer Gallery</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh11" name="swsh11" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh11" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh11-expansion-symbol.png);"></i>
                                    <span>Lost Origin</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="pgo" name="pgo" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="pgo" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/pgo-expansion-symbol.png);"></i>
                                    <span>Pokémon TCG: Pokémon GO</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh10tg" name="swsh10tg" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh10tg" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh10-expansion-symbol.png);"></i>
                                    <span>Astral Radiance Trainer Gallery</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh10" name="swsh10" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh10" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh10-expansion-symbol.png);"></i>
                                    <span>Astral Radiance</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh9tg" name="swsh9tg" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh9tg" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh9-expansion-symbol.png);"></i>
                                    <span>Brilliant Stars Trainer Gallery</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh9" name="swsh9" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh9" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh9-expansion-symbol.png);"></i>
                                    <span>Brilliant Stars</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh8" name="swsh8" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh8" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh8-expansion-symbol.png);"></i>
                                    <span>Fusion Strike</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="cel25c" name="cel25c" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="cel25c" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/25th-expansion-symbol.png);"></i>
                                    <span>Celebrations: Classic Collection</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="cel25" name="cel25" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="cel25" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/25th-expansion-symbol.png);"></i>
                                    <span>Celebrations</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh7" name="swsh7" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh7" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh7-expansion-symbol.png);"></i>
                                    <span>Evolving Skies</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh6" name="swsh6" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh6" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh6-expansion-symbol.png);"></i>
                                    <span>Chilling Reign</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh5" name="swsh5" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh5-expansion-symbol.png);"></i>
                                    <span>Battle Styles</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh45sv" name="swsh45sv" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh45sv" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh45sv-expansion-symbol.png);"></i>
                                    <span>Shining Fates: Shiny Vault</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh45" name="swsh45" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh45" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh45-expansion-symbol.png);"></i>
                                    <span>Shining Fates</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh4" name="swsh4" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh4-expansion-symbol.png);"></i>
                                    <span>Vivid Voltage</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh35" name="swsh35" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh35" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh35-expansion-symbol.png);"></i>
                                    <span>Champion’s Path</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh3" name="swsh3" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh3-expansion-symbol.png);"></i>
                                    <span>Darkness Ablaze</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh2" name="swsh2" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh2-expansion-symbol.png);"></i>
                                    <span>Rebel Clash</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="swsh1" name="swsh1" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swsh1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swsh1-expansion-symbol.png);"></i>
                                    <span>Sword &amp; Shield</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="swshp" name="swshp" class="pill-control__input" data-check-group="filtersword-shield[]" tabindex="-1">

                                <label for="swshp" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/swshp-expansion-symbol.png);"></i>
                                    <span>Sword &amp; Shield Promo</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm12" name="sm12" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm12" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm12-expansion-symbol.png);"></i>
                                    <span>Cosmic Eclipse</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sm115" name="sm115" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm115" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm115-expansion-symbol.png);"></i>
                                    <span>Hidden Fates</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm11" name="sm11" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm11" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm11-expansion-symbol.png);"></i>
                                    <span>Unified Minds</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm10" name="sm10" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm10" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm10-expansion-symbol.png);"></i>
                                    <span>Unbroken Bonds</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="det" name="det" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="det" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/det-expansion-symbol.png);"></i>
                                    <span>Detective Pikachu</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm9" name="sm9" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm9" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm9-expansion-symbol.png);"></i>
                                    <span>Team Up</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm8" name="sm8" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm8" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm8-expansion-symbol.png);"></i>
                                    <span>Lost Thunder</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sm75" name="sm75" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm75" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm75-expansion-symbol.png);"></i>
                                    <span>Dragon Majesty</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm7" name="sm7" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm7" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm7-expansion-symbol.png);"></i>
                                    <span>Celestial Storm</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm6" name="sm6" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm6" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm6-expansion-symbol.png);"></i>
                                    <span>Forbidden Light</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sm5" name="sm5" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm5-expansion-symbol.png);"></i>
                                    <span>Ultra Prism</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm4" name="sm4" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm4-expansion-symbol.png);"></i>
                                    <span>Crimson Invasion</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm35" name="sm35" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm35" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm35-expansion-symbol.png);"></i>
                                    <span>Shining Legends</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sm3" name="sm3" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm3-expansion-symbol.png);"></i>
                                    <span>Burning Shadows</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm2" name="sm2" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm2-expansion-symbol.png);"></i>
                                    <span>Guardians Rising</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="sm1" name="sm1" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sm1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sm1-expansion-symbol.png);"></i>
                                    <span>Sun &amp; Moon</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="sma" name="sma" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="sma" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/sma-expansion-symbol.png);"></i>
                                    <span>Yellow A Alternate</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="smp" name="smp" class="pill-control__input" data-check-group="filtersun-moon[]" tabindex="-1">

                                <label for="smp" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/smp-expansion-symbol.png);"></i>
                                    <span>Sun &amp; Moon Promo</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy12" name="xy12" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy12" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy12-expansion-symbol.png);"></i>
                                    <span>XY—Evolutions</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="xy11" name="xy11" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy11" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy11-expansion-symbol.png);"></i>
                                    <span>XY—Steam Siege</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy10" name="xy10" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy10" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy10-expansion-symbol.png);"></i>
                                    <span>XY—Fates Collide</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="g1" name="g1" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="g1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/g1-expansion-symbol.png);"></i>
                                    <span>Generations</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="xy9" name="xy9" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy9" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy9-expansion-symbol.png);"></i>
                                    <span>XY—BREAKpoint</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy8" name="xy8" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy8" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy8-expansion-symbol.png);"></i>
                                    <span>XY–BREAKthrough</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy7" name="xy7" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy7" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy7-expansion-symbol.png);"></i>
                                    <span>XY—Ancient Origins</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="xy6" name="xy6" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy6" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy6-expansion-symbol.png);"></i>
                                    <span>XY—Roaring Skies</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="dc1" name="dc1" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="dc1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dc1-expansion-symbol.png);"></i>
                                    <span>Double Crisis</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy5" name="xy5" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy5-expansion-symbol.png);"></i>
                                    <span>XY—Primal Clash</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="xy4" name="xy4" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy4-expansion-symbol.png);"></i>
                                    <span>XY—Phantom Forces</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy3" name="xy3" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy3-expansion-symbol.png);"></i>
                                    <span>XY—Furious Fists</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy2" name="xy2" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy2-expansion-symbol.png);"></i>
                                    <span>XY—Flashfire</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="xy1" name="xy1" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy1-expansion-symbol.png);"></i>
                                    <span>XY</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xy0" name="xy0" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xy0" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xy0-expansion-symbol.png);"></i>
                                    <span>XY—Kalos Starter Set</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="xya" name="xya" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xya" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/xya-expansion-symbol.png);"></i>
                                    <span>Yellow A Alternate</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="xyp" name="xyp" class="pill-control__input" data-check-group="filterxy[]" tabindex="-1">

                                <label for="xyp" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/black-star-promo.png);"></i>
                                    <span>XY—Promo</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw11" name="bw11" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw11" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw11-expansion-symbol.png);"></i>
                                    <span>BW—Legendary Treasures</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw10" name="bw10" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw10" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw10-expansion-symbol.png);"></i>
                                    <span>BW—Plasma Blast</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="bw9" name="bw9" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw9" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw9-expansion-symbol.png);"></i>
                                    <span>BW—Plasma Freeze</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw8" name="bw8" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw8" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw8-expansion-symbol.png);"></i>
                                    <span>BW—Plasma Storm</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw7" name="bw7" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw7" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw7-expansion-symbol.png);"></i>
                                    <span>BW—Boundaries Crossed</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="dv1" name="dv1" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="dv1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dv1-expansion-symbol.png);"></i>
                                    <span>Dragon Vault</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw6" name="bw6" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw6" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw6-expansion-symbol.png);"></i>
                                    <span>BW—Dragons Exalted</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw5" name="bw5" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw5-expansion-symbol.png);"></i>
                                    <span>BW—Dark Explorers</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="bw4" name="bw4" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw4-expansion-symbol.png);"></i>
                                    <span>BW—Next Destinies</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw3" name="bw3" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw3-expansion-symbol.png);"></i>
                                    <span>BW—Noble Victories</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bw2" name="bw2" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw2-expansion-symbol.png);"></i>
                                    <span>BW—Emerging Powers</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="bw1" name="bw1" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bw1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/bw1-expansion-symbol.png);"></i>
                                    <span>Black &amp; White</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="bwp" name="bwp" class="pill-control__input" data-check-group="filterblack-white[]" tabindex="-1">

                                <label for="bwp" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/black-star-promo.png);"></i>
                                    <span>BW—Promo</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="col1" name="col1" class="pill-control__input" data-check-group="filtercall-of-legends-hgss-series[]" tabindex="-1">

                                <label for="col1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/col1-expansion-symbol.png);"></i>
                                    <span>Call of Legends</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="hgss4" name="hgss4" class="pill-control__input" data-check-group="filtercall-of-legends-hgss-series[]" tabindex="-1">

                                <label for="hgss4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/hgss4-expansion-symbol.png);"></i>
                                    <span>Triumphant</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="hgss3" name="hgss3" class="pill-control__input" data-check-group="filtercall-of-legends-hgss-series[]" tabindex="-1">

                                <label for="hgss3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/hgss3-expansion-symbol.png);"></i>
                                    <span>Undaunted</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="hgss2" name="hgss2" class="pill-control__input" data-check-group="filtercall-of-legends-hgss-series[]" tabindex="-1">

                                <label for="hgss2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/hgss2-expansion-symbol.png);"></i>
                                    <span>Unleashed</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="hgss1" name="hgss1" class="pill-control__input" data-check-group="filtercall-of-legends-hgss-series[]" tabindex="-1">

                                <label for="hgss1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/hgss1-expansion-symbol.png);"></i>
                                    <span>HeartGold SoulSilver</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="hsp" name="hsp" class="pill-control__input" data-check-group="filtercall-of-legends-hgss-series[]" tabindex="-1">

                                <label for="hsp" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/black-star-promo.png);"></i>
                                    <span>HS—Promo</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="pl4" name="pl4" class="pill-control__input" data-check-group="filterplatinum[]" tabindex="-1">

                                <label for="pl4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/pl4-expansion-symbol.png);"></i>
                                    <span>Arceus</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="pl3" name="pl3" class="pill-control__input" data-check-group="filterplatinum[]" tabindex="-1">

                                <label for="pl3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/pl3-exp-symbol.png);"></i>
                                    <span>Supreme Victors</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="pl2" name="pl2" class="pill-control__input" data-check-group="filterplatinum[]" tabindex="-1">

                                <label for="pl2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/pl2-expansion-symbol.png);"></i>
                                    <span>Rising Rivals</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="pl1" name="pl1" class="pill-control__input" data-check-group="filterplatinum[]" tabindex="-1">

                                <label for="pl1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/pl1-expansion-symbol.png);"></i>
                                    <span>Platinum</span>
                                </label>
                        
                        </li>
                        
                            <li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="dp7" name="dp7" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp7" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp7-exp-symbol.png);"></i>
                                    <span>Stormfront</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="dp6" name="dp6" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp6" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp6-exp-symbol.png);"></i>
                                    <span>Legends Awakened</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="dp5" name="dp5" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp5-exp-symbol.png);"></i>
                                    <span>Majestic Dawn</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="dp4" name="dp4" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp4-expansion-symbol.png);"></i>
                                    <span>Great Encounters</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="dp3" name="dp3" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp3-expansion-symbol.png);"></i>
                                    <span>Secret Wonders</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="dp2" name="dp2" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp2-exp-symbol.png);"></i>
                                    <span>Mysterious Treasures</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="dp1" name="dp1" class="pill-control__input" data-check-group="filterdiamond-pearl[]" tabindex="-1">

                                <label for="dp1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/dp1-exp-symbol.png);"></i>
                                    <span>Diamond &amp; Pearl</span>
                                </label>
                        
                        </li>
                        
                            <li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex16" name="ex16" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex16" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-16symbol.png);"></i>
                                    <span>Power Keepers</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex15" name="ex15" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex15" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-15symbol.png);"></i>
                                    <span>Dragon Frontiers</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="ex14" name="ex14" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex14" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-14symbol.png);"></i>
                                    <span>Crystal Guardians</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex13" name="ex13" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex13" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-13symbol.png);"></i>
                                    <span>Holon Phantoms</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex12" name="ex12" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex12" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-12symbol.png);"></i>
                                    <span>Legend Maker</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="ex11" name="ex11" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex11" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-11symbol.png);"></i>
                                    <span>Delta Species</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex10" name="ex10" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex10" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-10symbol.png);"></i>
                                    <span>Unseen Forces</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex9" name="ex9" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex9" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-09symbol.png);"></i>
                                    <span>Emerald</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="ex8" name="ex8" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex8" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-08symbol.png);"></i>
                                    <span>Deoxys</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex7" name="ex7" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex7" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-07symbol.png);"></i>
                                    <span>Team Rocket Returns</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex6" name="ex6" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex6" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-06symbol.png);"></i>
                                    <span>Fire Red &amp; Leaf Green</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="ex5" name="ex5" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex5" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-05symbol.png);"></i>
                                    <span>Hidden Legends</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex4" name="ex4" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex4" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-04symbol.png);"></i>
                                    <span>Team Magma vs. Team Aqua</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex2" name="ex2" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex2" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-02symbol.png);"></i>
                                    <span>Sandstorm</span>
                                </label>
                        
                            </li><li class="middle list-grid-thirds pill-control">
                                <input type="checkbox" id="ex3" name="ex3" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex3" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-03symbol.png);"></i>
                                    <span>Dragon</span>
                                </label>
                        
                            </li><li class="list-grid-thirds pill-control">
                                <input type="checkbox" id="ex1" name="ex1" class="pill-control__input" data-check-group="filterex[]" tabindex="-1">

                                <label for="ex1" class="pill-control__label" tabindex="0">
                                    <i class="expansion" style="background-image: url(https://www.pokemon.com/static-assets/content-assets/cms/img/tcg/expansion-symbols/ex-01symbol.png);"></i>
                                    <span>Ruby &amp; Sapphire</span>
                                </label>
                        
                        </li>
'''

soup = BeautifulSoup(html_snippet, 'html.parser')

expansions = []
# Finden aller relevanten 'a'-Tags unter dem Filterpunkt "Expansions"
for a_tag in soup.select('i.expansion'):
    link = re.search(r'url\((.*?)\)', a_tag['style']).group(1)
    expansions.append(link)

names = []
for b_tag in soup.select('span'):
    name = b_tag.text
    names.append(name)

zipped = list(zip(names, expansions))

def download_expansions(list):
    for ext in list:
        filename = f"pokemon_ext/{ext[0]}.jpg"
        if not os.path.exists(filename):
            urllib.request.urlretrieve(ext[1], filename)
            print(f"Image saved: {filename}")
            time.sleep(5)


for expansion in zipped:
    print(expansion)
download_expansions(zipped)