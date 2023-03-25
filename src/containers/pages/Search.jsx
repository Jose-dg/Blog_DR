import BlogListSearch from 'components/blog/BlogListSearch';
import FullWidthLayout from 'hocs/layouts/FullWidthLayout';
import { useEffect } from 'react';
import { connect } from 'react-redux';
import { useParams } from 'react-router-dom';
import { search_blog } from 'redux/actions/blog';

function Search({
    search_blog,
    posts
}) {

    const params = useParams()
    const term = params.term

    useEffect(()=>{
        search_blog(term)
    }, [])

    return (
        <FullWidthLayout>
            <BlogListSearch blog_list={posts}/>
        </FullWidthLayout>
    );
}

const mapStateToProps = state => ({
    search_blog
})

export default connect(mapStateToProps,{

})(Search);