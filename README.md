<div id="top"></div>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]





<!-- PROJECT LOGO -->
<br />



  <h3 align="center">cBioportalDataClawler</h3>

  <p align="center">
    Some simple Python scripts to download data files from 
    <a href="https://github.com/othneildrew/Best-README-Template">https://www.cbioportal.org/</a> 
  </p>


</div>



<!-- ABOUT THE PROJECT -->

## About The Project

Some of cBioPortal datasets have no direct download link provided. For example, [China Pan-cancer (OrigiMed2020)](https://www.cbioportal.org/study?id=pan_origimed_2020) can not be downloaded by clicking the download button. So we wrote some Python scripts to download these datasets which are based on [cBioPortal Web API](https://www.cbioportal.org/webAPI) and [braovo](https://github.com/Yelp/bravado). 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

All Python scripts in this repository are based on Python 3 and braovo 11.0.3.

### Prerequisites

You should install Python 3 and bravado 11.0.3 before using these scripts.

* Bravado 11.0.3

  ```sh
  pip install bravado==11.0.3
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE -->

## Usage

To download, for example, the China Pan-cancer (OrigiMed2020) dataset, you can run the following command:

```sh
python3 chinapancancerdataclawler.py
```

It will download the data and generate three csv files "cna.csv", "mutations.csv" and "structual_variants.csv" under the same folder with ``` chinapancancerdataclawler.py ```.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Lijie Zhong -  ljzhong AT hku.hk

Project Link: [https://github.com/jasonwong-lab/cBioportalDataClawler](https://github.com/jasonwong-lab/cBioportalDataClawler)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/jasonwong-lab/cBioportalDataClawler.svg?style=for-the-badge
[contributors-url]: https://github.com/jasonwong-lab/cBioportalDataClawler/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jasonwong-lab/cBioportalDataClawler.svg?style=for-the-badge
[forks-url]: https://github.com/jasonwong-lab/cBioportalDataClawler/network/members
[stars-shield]: https://img.shields.io/github/stars/jasonwong-lab/cBioportalDataClawler.svg?style=for-the-badge
[stars-url]: https://github.com/jasonwong-lab/cBioportalDataClawler/stargazers
[issues-shield]: https://img.shields.io/github/issues/jasonwong-lab/cBioportalDataClawler.svg?style=for-the-badge
[issues-url]: https://github.com/jasonwong-lab/cBioportalDataClawler/issues
[license-shield]: https://img.shields.io/github/license/jasonwong-lab/cBioportalDataClawler.svg?style=for-the-badge
[license-url]: https://github.com/jasonwong-lab/cBioportalDataClawler/blob/main/LICENSE
