import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import store from './store';

import Home from './containers/pages/Home';
import Error404 from './containers/errors/Error404';

import Blog from './containers/pages/blog/Blog';
import BlogPost from 'containers/pages/blog/BlogPost';
import BlogCategory from 'containers/pages/blog/category/BlogCategory';
import Search from 'containers/pages/Search';

import Contact from 'containers/pages/contact/Contact';
import Connect from 'containers/pages/Connect';
// import Datasets from 'containers/pages/datasets/Datasets';
import Servicios from 'containers/pages/servicios/Servicios';
import Nosotros from 'containers/pages/nosotros/Nosotros';
import Courses from 'containers/pages/courses/Courses';

function App() {
    return (
        <Provider store={store}>
            <Router>
                <Routes>
                    {/* Error Display */}
                    <Route path='*' element={<Error404/>}/>

                    {/* Home Display */}
                    <Route path='/' element={<Home/>}/>
                    <Route path='/blog' element={<Blog/>}/>
                    <Route path='/blog/post/:slug' element={<BlogPost/>}/>
                    <Route path='/blog/categories/:category_id' element={<BlogCategory/>}/>

                    <Route path='/search/:term' element={<Search/>}/>

                    {/* <Route path='/datasets' element={<Datasets/>}/> */}

                    
                    <Route path='/courses' element={<Courses/>}/>
                    <Route path='/servicios' element={<Servicios/>}/>
                    <Route path='/nosotros' element={<Nosotros/>}/>
                    {/* <Route path='/privacidad' element={<Privacy/>}/> */}
                    {/* <Route path='/terminos' element={<Terms/>}/> */}



                    <Route path='/contact' element={<Contact/>}/>
                    <Route path='/connect' element={<Connect/>}/>
                     
                </Routes>
            </Router>
        </Provider>
    );
}

export default App;





